# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_17:53:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 17:53:12 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:16:16 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.036 |  |
| 2026-05-11 17:15:40 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.044 |  |
| 2026-05-11 17:14:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 17:14:52 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 17:14:47 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.025 |  |
| 2026-05-11 17:14:24 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.011 |  |
| 2026-05-11 17:10:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.027 |  |
| 2026-05-11 17:10:01 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:09:53 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:09:22 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.064 |  |
| 2026-05-11 17:09:04 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-11 17:08:51 | Katharagama (Menik Ganga) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 17:07:35 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.113 |  |
| 2026-05-11 17:07:08 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.069 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 17:14:53 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-11 17:04:59 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.482 | 🔺 Rising |
| 2026-05-11 17:02:22 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.362 | 🔺 Rising |
| 2026-05-11 17:04:56 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-05-11 17:05:44 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-05-11 17:01:38 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-05-11 17:01:46 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-11 17:05:01 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-11 17:07:08 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-11 17:00:57 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-11 17:09:04 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-11 17:02:12 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-11 17:02:02 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 17:02:51 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 17:08:51 | Katharagama (Menik Ganga) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 17:02:57 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 17:04:21 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 17:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:09:53 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:01:48 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:04:51 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:10:01 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:00:20 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:53:12 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-11 17:05:25 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-11 17:14:24 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.011 |  |
| 2026-05-11 17:14:47 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.025 |  |
| 2026-05-11 17:10:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.027 |  |
| 2026-05-11 17:02:30 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-05-11 17:16:16 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.036 |  |
| 2026-05-11 17:01:56 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.039 |  |
| 2026-05-11 17:15:40 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.044 |  |
| 2026-05-11 17:00:17 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.045 |  |
| 2026-05-11 17:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.72 | 🟢 Normal | -0.048 |  |
| 2026-05-11 17:09:22 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.064 |  |
| 2026-05-11 17:01:04 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.064 |  |
| 2026-05-11 17:02:45 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.082 |  |
| 2026-05-11 17:03:38 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.109 |  |
| 2026-05-11 17:07:35 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)