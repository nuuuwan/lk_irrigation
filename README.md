# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_00:14:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 00:14:25 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 00:14:19 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-10-30 00:09:36 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.035 |  |
| 2026-10-30 00:08:51 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:08:31 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | -0.012 |  |
| 2026-10-30 00:08:07 | Pitabeddara (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-30 00:07:39 | Baddegama (Gin Ganga) | 3.78 | 🟡 Alert | -0.029 |  |
| 2026-10-30 00:07:25 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:06:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:06:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 00:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:05:53 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.000 |  |
| 2026-10-30 00:05:52 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-10-30 00:05:44 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | -0.019 |  |
| 2026-10-30 00:05:39 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.047 |  |
| 2026-10-30 00:05:38 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:05:26 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:04:35 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -72.000 |  |
| 2026-10-30 00:04:34 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -72.000 |  |
| 2026-10-30 00:04:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:04:04 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 00:03:49 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:03:44 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:03:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:03:20 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:02:39 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-10-30 00:02:29 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-30 00:02:29 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-30 00:02:22 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 00:02:16 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:02:16 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:02:09 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-10-30 00:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:01:26 | Rathnapura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.114 |  |
| 2026-10-30 00:01:05 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.171 |  |
| 2026-10-30 00:00:57 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.220 |  |
| 2026-10-30 00:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-29 23:58:13 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.220 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 00:14:25 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 00:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 00:05:53 | Putupaula (Kalu Ganga) | 3.62 | 🟡 Alert | 0.000 |  |
| 2026-10-30 00:08:31 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | -0.012 |  |
| 2026-10-30 00:07:39 | Baddegama (Gin Ganga) | 3.78 | 🟡 Alert | -0.029 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-30 00:06:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 00:08:07 | Pitabeddara (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-30 00:02:22 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 00:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:05:26 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:04:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:03:20 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:03:49 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:06:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:05:38 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 23:02:32 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-30 00:14:19 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-10-30 00:05:52 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-10-30 00:07:25 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:08:51 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:03:44 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:02:16 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:04:04 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-30 00:05:44 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | -0.019 |  |
| 2026-10-30 00:02:39 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-10-30 00:02:29 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-30 00:02:29 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-30 00:02:09 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-10-30 00:09:36 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.035 |  |
| 2026-10-30 00:05:39 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.047 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-30 00:01:26 | Rathnapura (Kalu Ganga) | 3.99 | 🟢 Normal | -0.114 |  |
| 2026-10-30 00:01:05 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.171 |  |
| 2026-10-30 00:00:57 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.220 |  |
| 2026-10-30 00:04:35 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)