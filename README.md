# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_11:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 11:03:07 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:03:07 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.093 |  |
| 2026-11-18 11:02:51 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.043 |  |
| 2026-11-18 11:02:50 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:45 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:43 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.016 |  |
| 2026-11-18 11:02:14 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:14 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 11:02:10 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:01:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:54 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.062 |  |
| 2026-11-18 11:01:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:55 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:38 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:00:38 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-18 11:00:22 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:13 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:31:05 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:29:00 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 11:02:14 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 11:00:13 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:47 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:50 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:22 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:06:02 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:51 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:04:42 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:13:01 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:32 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:02:14 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:02:28 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:00:55 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 11:01:54 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 10:31:05 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-18 10:05:23 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:04:53 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:06:18 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:08 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:45 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:03:07 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:02:10 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 11:00:38 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 10:04:23 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-11-18 11:00:38 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-18 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.016 |  |
| 2026-11-18 10:04:04 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.020 |  |
| 2026-11-18 10:04:44 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.028 |  |
| 2026-11-18 10:01:40 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-18 10:04:11 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:02:43 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-11-18 11:03:07 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2026-11-18 11:02:51 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.043 |  |
| 2026-11-18 10:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.061 |  |
| 2026-11-18 11:01:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.062 |  |
| 2026-11-18 11:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)