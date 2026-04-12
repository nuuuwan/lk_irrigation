# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_18:34:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 18:34:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:18:07 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:18:01 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.066 |  |
| 2026-04-12 18:14:35 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 18:12:38 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-12 18:10:30 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 18:07:38 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:07:06 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:07:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-04-12 18:07:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:07:01 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:06:31 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:06:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 18:06:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 18:05:25 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 18:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.048 |  |
| 2026-04-12 18:04:35 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-04-12 18:04:21 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:04:07 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.012 |  |
| 2026-04-12 18:04:05 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-04-12 18:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:03:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:03:12 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:02:50 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:40 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-12 18:02:24 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 18:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:19 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:02:01 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-04-12 18:01:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:01:33 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 18:01:21 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:00:55 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:00:22 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 18:00:16 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-12 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:00:11 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 18:02:40 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-12 18:02:01 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-04-12 18:12:38 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 18:00:22 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 18:02:50 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-12 18:00:16 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-12 18:06:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 18:01:33 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 18:02:24 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 18:05:25 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 18:07:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:03:12 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:06:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 18:03:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:34:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:10:30 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:07:38 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:04:21 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:03:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:18:07 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:14:35 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:00:55 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:01:21 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:06:31 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:00:11 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:07:01 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:02:19 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-12 18:04:05 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-04-12 18:04:07 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.012 |  |
| 2026-04-12 18:04:35 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-04-12 18:07:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 18:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.048 |  |
| 2026-04-12 18:18:01 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)