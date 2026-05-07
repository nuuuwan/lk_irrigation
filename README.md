# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_09:16:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,151 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 09:16:56 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:13:13 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-07 09:10:17 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-05-07 09:09:54 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.107 |  |
| 2026-05-07 09:09:07 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-05-07 09:09:00 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.028 |  |
| 2026-05-07 09:07:43 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-07 09:07:24 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.206 |  |
| 2026-05-07 09:07:08 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-07 09:06:38 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.044 |  |
| 2026-05-07 09:06:18 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.027 |  |
| 2026-05-07 09:06:04 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-07 09:05:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:04:18 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.107 |  |
| 2026-05-07 09:03:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:03:26 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 09:03:25 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:03:15 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.097 |  |
| 2026-05-07 09:03:14 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-05-07 09:03:08 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 09:02:59 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.067 |  |
| 2026-05-07 09:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:02:37 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-07 09:02:34 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-07 09:02:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-07 09:02:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-07 09:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-07 09:01:46 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 09:01:44 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-05-07 09:01:42 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.053 |  |
| 2026-05-07 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-05-07 09:01:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.050 |  |
| 2026-05-07 09:00:55 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:00:48 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.104 |  |
| 2026-05-07 09:00:43 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 09:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-07 09:00:25 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 09:06:04 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-07 09:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-07 09:03:26 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 09:00:43 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 09:02:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-07 09:07:08 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-07 09:03:08 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 09:02:34 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-07 09:00:25 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 09:01:46 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 09:13:13 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-07 09:01:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:03:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:08:36 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:16:56 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:02:59 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:03:25 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:02:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:05:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:00:55 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-07 09:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-07 09:06:18 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.027 |  |
| 2026-05-07 09:09:00 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.028 |  |
| 2026-05-07 09:07:43 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-07 09:10:17 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-05-07 09:02:37 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-07 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-05-07 09:03:14 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2026-05-07 09:01:44 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-05-07 09:06:38 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.044 |  |
| 2026-05-07 09:09:07 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-05-07 09:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.050 |  |
| 2026-05-07 09:01:42 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.053 |  |
| 2026-05-07 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.067 |  |
| 2026-05-07 09:03:15 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.097 |  |
| 2026-05-07 09:02:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-07 09:00:48 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.104 |  |
| 2026-05-07 09:09:54 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.107 |  |
| 2026-05-07 09:07:24 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)