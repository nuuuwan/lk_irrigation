# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_17:19:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 17:19:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:11:46 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:10:59 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-06-24 17:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:09:07 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:08:24 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:07:21 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-06-24 17:06:59 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.078 |  |
| 2026-06-24 17:06:58 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-06-24 17:06:54 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-24 17:06:52 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:05:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.043 |  |
| 2026-06-24 17:05:20 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:04:38 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.050 |  |
| 2026-06-24 17:03:42 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-06-24 17:03:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 17:03:29 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.060 |  |
| 2026-06-24 17:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.098 |  |
| 2026-06-24 17:02:47 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:44 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.016 |  |
| 2026-06-24 17:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:02:36 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:28 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:02:19 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-24 17:02:10 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2026-06-24 17:02:10 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.040 |  |
| 2026-06-24 17:02:00 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:57 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:37 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 17:01:27 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:08 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:33 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:00:20 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:16 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:13 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 17:02:19 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-24 17:03:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 17:06:54 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-24 17:01:37 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 17:00:13 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:27 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:08 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:19:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:06:52 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:08:24 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:05:20 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:36 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:57 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:01:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:00 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:47 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:11:46 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:09:07 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:20 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:00:16 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 17:02:28 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:02:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:00:33 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-24 17:02:10 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2026-06-24 17:02:44 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.016 |  |
| 2026-06-24 17:07:21 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-06-24 17:10:59 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-06-24 17:02:10 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.040 |  |
| 2026-06-24 17:03:42 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-06-24 17:06:58 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-06-24 17:05:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.043 |  |
| 2026-06-24 17:04:38 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.050 |  |
| 2026-06-24 17:03:29 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.060 |  |
| 2026-06-24 17:06:59 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.078 |  |
| 2026-06-24 17:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)