# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_09:18:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 09:18:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.016 |  |
| 2026-09-28 09:14:09 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.040 |  |
| 2026-09-28 09:10:55 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.028 |  |
| 2026-09-28 09:10:45 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | -0.009 |  |
| 2026-09-28 09:09:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:08:25 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-09-28 09:07:52 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2026-09-28 09:07:46 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-09-28 09:07:39 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.041 |  |
| 2026-09-28 09:07:30 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-09-28 09:06:47 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:06:36 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:05:35 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:04:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:04:04 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-09-28 09:03:50 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-09-28 09:03:48 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.020 |  |
| 2026-09-28 09:03:47 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-09-28 09:03:24 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.079 |  |
| 2026-09-28 09:03:19 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-09-28 09:03:16 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:03:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.079 |  |
| 2026-09-28 09:03:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:00 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:02:51 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.173 |  |
| 2026-09-28 09:02:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-09-28 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:01:37 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:01:37 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-09-28 09:01:25 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.060 |  |
| 2026-09-28 09:00:50 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:00:37 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:00:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 09:10:55 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.028 |  |
| 2026-09-28 09:14:09 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.040 |  |
| 2026-09-28 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.079 |  |
| 2026-09-28 09:00:50 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:47 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:00:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:09:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:06:36 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:04:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:04:04 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:03:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:01:37 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:00:37 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:06:47 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:07:30 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-09-28 09:10:45 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | -0.009 |  |
| 2026-09-28 09:05:35 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:03:00 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:03:16 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-28 09:03:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-09-28 09:08:25 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-09-28 09:07:46 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-09-28 09:18:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.016 |  |
| 2026-09-28 09:03:48 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.020 |  |
| 2026-09-28 08:05:53 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-09-28 09:03:50 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-09-28 09:07:52 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.021 |  |
| 2026-09-28 09:01:37 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-09-28 09:03:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-09-28 09:02:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-09-28 09:03:19 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-09-28 09:07:39 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.041 |  |
| 2026-09-28 09:01:25 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.060 |  |
| 2026-09-28 09:03:24 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.079 |  |
| 2026-09-28 09:02:51 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)