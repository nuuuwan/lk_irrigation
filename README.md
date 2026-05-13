# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_10:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,565 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 10:02:54 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:02:50 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.029 |  |
| 2026-05-13 10:02:48 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -1.067 |  |
| 2026-05-13 10:02:37 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 10:02:26 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 10:02:20 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:01:52 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:01:41 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-13 10:01:34 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-13 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.060 |  |
| 2026-05-13 10:01:12 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-13 10:01:11 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 10:00:39 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 10:00:36 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.032 |  |
| 2026-05-13 10:00:20 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-13 09:15:35 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -1.067 |  |
| 2026-05-13 09:14:20 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-13 09:12:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.078 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 09:01:56 | Pitabeddara (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.816 | 🔺 Rising |
| 2026-05-13 09:08:18 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | 0.562 | 🔺 Rising |
| 2026-05-13 09:08:55 | Magura (Kalu Ganga) | 3.79 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-05-13 09:14:20 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-13 10:01:12 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-13 09:07:51 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-05-13 09:03:33 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-13 09:08:34 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-13 09:06:12 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-13 10:01:41 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-13 09:03:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-13 09:12:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-13 09:07:54 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-13 09:08:11 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-13 09:06:22 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-13 10:02:26 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 10:02:37 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 10:00:39 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 10:01:11 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 09:08:17 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:01:52 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:02:54 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 10:02:20 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 09:08:40 | Katharagama (Menik Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-05-13 10:01:34 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-13 09:05:43 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-05-13 10:00:20 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-05-13 09:08:51 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-05-13 10:02:50 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.029 |  |
| 2026-05-13 09:04:47 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-05-13 09:05:42 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-05-13 10:00:36 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.032 |  |
| 2026-05-13 09:00:52 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.034 |  |
| 2026-05-13 09:01:25 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-05-13 09:04:46 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.040 |  |
| 2026-05-13 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.060 |  |
| 2026-05-13 09:04:35 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.225 |  |
| 2026-05-13 10:02:48 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -1.067 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)