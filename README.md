# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_16:26:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 16:26:08 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.035 |  |
| 2026-05-08 16:26:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-08 16:13:27 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:10:16 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-08 16:09:19 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-05-08 16:09:11 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.029 |  |
| 2026-05-08 16:09:08 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.030 |  |
| 2026-05-08 16:08:21 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 16:07:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-08 16:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.117 |  |
| 2026-05-08 16:06:02 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 16:05:28 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 16:26:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-08 16:09:19 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-05-08 16:07:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-05-08 16:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-05-08 16:04:44 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-08 16:03:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-08 16:10:16 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-08 16:04:16 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-08 16:03:56 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 16:04:16 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-08 16:04:14 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-08 16:08:21 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 16:06:02 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 16:03:22 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:02:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:04:36 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:02:45 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:05:28 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:02:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:13:27 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 16:05:10 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:02:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-08 16:01:37 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-08 16:00:17 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-08 16:00:33 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-08 16:02:47 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-05-08 16:09:11 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.029 |  |
| 2026-05-08 16:09:08 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.030 |  |
| 2026-05-08 16:02:53 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.030 |  |
| 2026-05-08 16:03:02 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.031 |  |
| 2026-05-08 16:26:08 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.035 |  |
| 2026-05-08 16:03:52 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-05-08 15:07:06 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.047 |  |
| 2026-05-08 16:03:39 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.070 |  |
| 2026-05-08 16:03:26 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.070 |  |
| 2026-05-08 16:03:57 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.081 |  |
| 2026-05-08 16:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.117 |  |
| 2026-05-08 16:05:10 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)