# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_18:07:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,814 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 18:07:40 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | -0.039 |  |
| 2026-11-14 18:06:22 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:05:37 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:05:27 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.039 |  |
| 2026-11-14 18:05:26 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:45 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:23 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:05 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:03:58 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.030 |  |
| 2026-11-14 18:03:19 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 18:03:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.080 |  |
| 2026-11-14 18:03:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-11-14 18:02:59 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-11-14 18:02:50 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-14 18:02:37 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:36 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:34 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.017 |  |
| 2026-11-14 18:02:31 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:02:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-11-14 18:02:15 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:12 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-14 18:02:12 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.041 |  |
| 2026-11-14 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.111 |  |
| 2026-11-14 18:02:08 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:02 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:54 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 18:01:48 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:47 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:37 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:29 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.012 |  |
| 2026-11-14 18:01:27 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:26 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:10 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 18:03:19 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 18:03:58 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.030 |  |
| 2026-11-14 18:02:50 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 18:01:54 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:45 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:05:37 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:15 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:06:22 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:08 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:27 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:01:48 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:36 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:23 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:02 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:02:37 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:00:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:04:05 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:02:31 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:37 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:01:47 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:10 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:01:29 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.012 |  |
| 2026-11-14 18:02:34 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.017 |  |
| 2026-11-14 18:02:59 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-11-14 18:02:12 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-14 18:02:22 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-11-14 18:05:26 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-11-14 18:01:26 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-14 18:03:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-11-14 18:05:27 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.039 |  |
| 2026-11-14 18:07:40 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | -0.039 |  |
| 2026-11-14 18:02:12 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.041 |  |
| 2026-11-14 18:03:11 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.080 |  |
| 2026-11-14 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)