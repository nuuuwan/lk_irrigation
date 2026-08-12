# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_18:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,673 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 18:10:13 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 18:09:02 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:27 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:14 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.125 |  |
| 2026-08-12 18:04:28 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 18:04:18 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:04:09 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.110 |  |
| 2026-08-12 18:04:05 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 18:03:52 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.042 |  |
| 2026-08-12 18:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:03:39 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:03:11 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-12 18:03:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:03:02 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-12 18:03:01 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-12 18:02:55 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-08-12 18:02:47 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-08-12 18:02:45 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:02:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 18:02:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:27 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.035 |  |
| 2026-08-12 18:02:25 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:02:08 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:05 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:59 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-08-12 18:01:57 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-12 18:01:43 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:21 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:18 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.035 |  |
| 2026-08-12 18:01:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2026-08-12 18:01:06 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:00:29 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:00:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:59:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-12 17:35:14 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:35:13 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 18:03:02 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-12 18:01:57 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-12 18:03:01 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-12 18:10:13 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 17:59:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-12 17:01:24 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 18:04:28 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 18:02:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 18:04:05 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 18:00:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:03:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:08 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:06 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:00:29 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:14 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:27 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:03:39 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:43 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:02:05 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:21 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:09:02 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-08-12 18:03:11 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-12 18:02:55 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-08-12 18:02:45 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:02:25 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-08-12 18:02:47 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-08-12 18:01:59 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 18:02:27 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.035 |  |
| 2026-08-12 18:01:18 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.035 |  |
| 2026-08-12 18:03:52 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.042 |  |
| 2026-08-12 18:01:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2026-08-12 18:04:09 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.110 |  |
| 2026-08-12 18:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)