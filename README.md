# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_19:22:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,397 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 19:22:44 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 5.382 | 🔺 Rising |
| 2026-06-14 19:21:15 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-06-14 19:14:22 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:12:42 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-06-14 19:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.027 |  |
| 2026-06-14 19:08:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-06-14 19:08:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-06-14 19:07:05 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-14 19:06:40 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:06:19 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-06-14 19:06:06 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-06-14 19:05:54 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.047 |  |
| 2026-06-14 19:05:49 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-06-14 19:05:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:05:24 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 19:05:09 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:04:56 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.060 |  |
| 2026-06-14 19:04:48 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:04:34 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-14 19:04:27 | Panadugama (Nilwala Ganga) | 0.96 | 🟢 Normal | 5.382 | 🔺 Rising |
| 2026-06-14 19:03:36 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:29 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.117 |  |
| 2026-06-14 19:03:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-06-14 19:03:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:00 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-06-14 19:02:37 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.041 |  |
| 2026-06-14 19:02:26 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:02:24 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.027 |  |
| 2026-06-14 19:02:17 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-06-14 19:02:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.040 |  |
| 2026-06-14 19:02:01 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:01:41 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | -19.059 |  |
| 2026-06-14 19:01:33 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-06-14 19:01:24 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -19.059 |  |
| 2026-06-14 19:01:22 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-06-14 19:01:18 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 19:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | -0.027 |  |
| 2026-06-14 19:06:19 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-06-14 19:22:44 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 5.382 | 🔺 Rising |
| 2026-06-14 19:07:05 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-14 19:04:34 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-14 19:05:24 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:02:26 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:05:09 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:14:22 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:04:48 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:02:01 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:06:40 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:03:36 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:05:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:01:18 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:21:15 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-06-14 19:12:42 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-06-14 19:08:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 19:01:33 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-06-14 19:06:06 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-14 19:02:24 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.027 |  |
| 2026-06-14 19:02:17 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-06-14 19:03:00 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-06-14 19:01:22 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-06-14 19:02:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.040 |  |
| 2026-06-14 19:02:37 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.041 |  |
| 2026-06-14 19:08:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-06-14 19:05:54 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.047 |  |
| 2026-06-14 19:04:56 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.060 |  |
| 2026-06-14 19:03:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.097 |  |
| 2026-06-14 19:03:29 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.117 |  |
| 2026-06-14 19:01:41 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | -19.059 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)