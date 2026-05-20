# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_21:12:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 21:12:08 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:11:58 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-20 21:10:38 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:08:52 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-20 21:08:47 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:07:49 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-05-20 21:05:49 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-20 21:05:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:09 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:02 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-20 21:04:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.024 |  |
| 2026-05-20 21:04:22 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 21:04:04 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:03:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 21:03:37 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 21:03:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-05-20 21:03:17 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:11 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:02:58 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:02:19 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 21:02:11 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 21:02:05 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:01:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-20 21:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:01:24 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-05-20 21:01:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:01:08 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-20 21:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:00:38 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 21:11:58 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-20 21:01:47 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-20 21:01:08 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-20 21:02:11 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-20 21:08:52 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-20 21:04:22 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 21:05:49 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-20 21:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 21:03:37 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 21:03:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 21:05:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:00:38 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:17 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:03:11 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:10:38 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:08:47 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:02:05 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:01:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 20:13:02 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:05:09 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 21:12:08 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:02:58 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-20 20:06:10 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:02:19 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:04:04 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-20 21:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-20 20:05:07 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-05-20 21:01:24 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-20 21:05:02 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-20 21:04:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.024 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 21:07:49 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-05-20 21:03:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)