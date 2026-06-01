# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_14:18:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 14:18:20 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:16:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-01 14:11:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:10:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:09:43 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:07:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:06:39 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-06-01 14:05:45 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-01 14:05:33 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:05:04 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:04:55 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:04:30 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:04:05 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-01 14:03:59 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:55 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:52 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:03:50 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-06-01 14:03:44 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-01 14:03:30 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:23 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:17 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:11 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:02:47 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:02:28 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.072 |  |
| 2026-06-01 14:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-01 14:02:11 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-01 14:02:00 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:52 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:52 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 14:01:42 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:30 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:01:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:00 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:00:46 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 14:05:45 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-01 14:03:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-01 14:16:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-01 14:02:11 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-01 14:01:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 14:10:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:52 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:44 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:02:28 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:11:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:17 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:23 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:07:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:55 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:18:20 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:04:55 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:30 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:04:30 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:03:59 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:00 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:02:00 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:00:46 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 14:01:42 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:02:47 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:01:52 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:03:52 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:05:04 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-01 14:01:30 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:03:11 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:09:43 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-06-01 14:06:39 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-06-01 14:03:50 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-06-01 14:04:05 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-01 14:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-01 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)