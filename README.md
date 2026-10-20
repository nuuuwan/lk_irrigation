# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_11:35:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 11:35:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:14:15 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-10-20 11:11:38 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.026 |  |
| 2026-10-20 11:10:28 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-10-20 11:09:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:06:28 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:06:27 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-20 11:06:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:05:57 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-10-20 11:05:56 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:05:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:05:37 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 11:05:02 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:41 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:41 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.029 |  |
| 2026-10-20 11:03:37 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:03:32 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.050 |  |
| 2026-10-20 11:03:31 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-10-20 11:03:20 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:13 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.062 |  |
| 2026-10-20 11:03:07 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 11:03:05 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:02:46 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:02:39 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-10-20 11:02:09 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:01:55 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.030 |  |
| 2026-10-20 11:01:51 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.012 |  |
| 2026-10-20 11:01:34 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:01:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.100 |  |
| 2026-10-20 11:01:31 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 11:01:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-10-20 11:01:14 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:00:57 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:00:53 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:00:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.059 |  |
| 2026-10-20 11:00:50 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-20 11:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:00:11 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 11:00:11 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.023 |  |
| 2026-10-20 11:10:28 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-10-20 11:03:07 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 11:01:31 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 11:00:50 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-20 11:05:37 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 11:01:14 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:06:28 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:41 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:09:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:02:46 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:05:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:03:20 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:05:02 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:02:09 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:35:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-10-20 11:14:15 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-10-20 11:05:56 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:01:34 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:06:11 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:03:37 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:03:05 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-20 11:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:00:57 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:00:53 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-10-20 11:01:51 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.012 |  |
| 2026-10-20 11:02:39 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-10-20 11:06:27 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-20 11:01:15 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-10-20 11:11:38 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.026 |  |
| 2026-10-20 11:03:41 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.029 |  |
| 2026-10-20 11:01:55 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.030 |  |
| 2026-10-20 11:03:31 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-10-20 11:05:57 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-10-20 11:03:32 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.050 |  |
| 2026-10-20 11:00:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.059 |  |
| 2026-10-20 11:03:13 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.062 |  |
| 2026-10-20 11:01:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)