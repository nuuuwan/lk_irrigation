# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_22:29:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 22:29:30 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.015 |  |
| 2026-10-30 22:21:26 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:19:25 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.016 |  |
| 2026-10-30 22:15:26 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.124 |  |
| 2026-10-30 22:13:51 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:11:11 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.017 |  |
| 2026-10-30 22:09:16 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.028 |  |
| 2026-10-30 22:08:32 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.132 |  |
| 2026-10-30 22:08:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:07:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:07:25 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:06:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:05:31 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.034 |  |
| 2026-10-30 22:05:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:05:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-10-30 22:05:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:04:48 | Putupaula (Kalu Ganga) | 3.13 | 🟡 Alert | -0.010 |  |
| 2026-10-30 22:04:40 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:04:21 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | -0.041 |  |
| 2026-10-30 22:03:15 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-30 22:03:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.064 |  |
| 2026-10-30 22:02:56 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:02:55 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:46 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:25 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:02:21 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 22:02:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:01:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:01:39 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:01:35 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:01:27 | Thalgahagoda (Nilwala Ganga) | 1.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-30 22:01:02 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-30 22:00:31 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:00:08 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-10-30 21:53:36 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 22:01:27 | Thalgahagoda (Nilwala Ganga) | 1.77 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-30 22:04:48 | Putupaula (Kalu Ganga) | 3.13 | 🟡 Alert | -0.010 |  |
| 2026-10-30 22:09:16 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.028 |  |
| 2026-10-30 22:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | -0.041 |  |
| 2026-10-30 22:03:15 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-30 22:01:02 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-30 22:02:21 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 22:06:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:01:35 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:08:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:02:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:04:21 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:21:26 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:13:51 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:07:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:05:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:02:25 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:01:39 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:05:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 22:04:40 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:07:25 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:46 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:02:55 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:00:31 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:01:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-30 22:29:30 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.015 |  |
| 2026-10-30 22:19:25 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.016 |  |
| 2026-10-30 22:11:11 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.017 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 22:00:08 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-10-30 22:05:31 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.034 |  |
| 2026-10-30 22:05:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-10-30 22:03:02 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.064 |  |
| 2026-10-30 22:15:26 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | -0.124 |  |
| 2026-10-30 22:08:32 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)