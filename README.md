# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_13:04:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 13:04:38 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.043 |  |
| 2026-05-11 13:04:26 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-11 13:04:00 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 13:03:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:03:32 | Thanamalwila (Kirindi Oya) | 2.47 | 🟢 Normal | -0.082 |  |
| 2026-05-11 13:03:31 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:03:30 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-11 13:03:11 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-11 13:03:08 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.115 |  |
| 2026-05-11 13:03:05 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-11 13:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-05-11 13:02:35 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.078 |  |
| 2026-05-11 13:02:29 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.049 |  |
| 2026-05-11 13:02:27 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-11 13:02:18 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:02:02 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:00:57 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 13:00:46 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 12:53:17 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:23:18 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:16:20 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.106 |  |
| 2026-05-11 12:13:26 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 12:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-11 12:08:57 | Moragaswewa (Deduru Oya) | 1.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-11 12:03:57 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 12:03:29 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-11 12:02:13 | Katharagama (Menik Ganga) | 2.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-11 13:03:30 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-11 12:06:50 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-11 12:03:12 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-11 12:02:36 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 12:07:01 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 13:04:26 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-11 13:04:00 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 12:07:09 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 13:00:57 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 13:02:02 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:02:08 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:01:22 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:02:18 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:03:31 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:02:36 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:03:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-11 12:06:05 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 13:03:05 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-11 13:03:11 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-11 13:02:27 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-11 12:06:01 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-05-11 13:00:46 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-11 13:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-05-11 12:05:04 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-05-11 12:03:31 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-05-11 13:04:38 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.043 |  |
| 2026-05-11 12:03:52 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.044 |  |
| 2026-05-11 13:02:29 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.049 |  |
| 2026-05-11 12:04:06 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.063 |  |
| 2026-05-11 13:02:35 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.078 |  |
| 2026-05-11 13:03:32 | Thanamalwila (Kirindi Oya) | 2.47 | 🟢 Normal | -0.082 |  |
| 2026-05-11 12:16:20 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.106 |  |
| 2026-05-11 13:03:08 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.115 |  |
| 2026-05-11 12:05:36 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)