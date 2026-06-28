# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_10:33:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 10:33:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:19:28 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-06-28 10:18:22 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-06-28 10:16:15 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:14:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:13:55 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:10:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 10:10:34 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.036 |  |
| 2026-06-28 10:10:16 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:10:10 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 10:09:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:06:52 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:06:29 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:06:06 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:05:42 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:05:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-28 10:05:25 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:04:20 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-06-28 10:04:13 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:03:45 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.107 |  |
| 2026-06-28 10:03:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 10:03:23 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:03:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:02:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:02:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:02:16 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 10:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:01:49 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:01:35 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-06-28 10:01:09 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:01:06 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-28 10:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 10:00:53 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:00:50 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.021 |  |
| 2026-06-28 10:00:48 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-06-28 10:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:00:35 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:00:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 09:59:09 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 10:05:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-28 10:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 10:10:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 10:10:10 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 10:02:16 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 10:03:33 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 10:01:09 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:10:16 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:01:49 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:33:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:14:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:02:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:00:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:13:55 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:05:25 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:00:35 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:04:13 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:06:29 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:16:15 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:00:53 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:06:52 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:05:42 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:03:12 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 10:19:28 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-06-28 10:18:22 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-06-28 10:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:02:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:09:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:03:23 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-28 10:04:20 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-06-28 10:01:06 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-28 10:00:48 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-06-28 10:00:50 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.021 |  |
| 2026-06-28 10:01:35 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-06-28 10:10:34 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.036 |  |
| 2026-06-28 10:03:45 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)