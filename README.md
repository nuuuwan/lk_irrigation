# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_08:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 08:11:42 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-15 08:10:10 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:09:57 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-10-15 08:09:52 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:08:31 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-15 08:08:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 08:07:48 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-15 08:07:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:07:04 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-10-15 08:06:28 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.276 |  |
| 2026-10-15 08:06:21 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.019 |  |
| 2026-10-15 08:05:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:05:52 | Rathnapura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.033 |  |
| 2026-10-15 08:05:38 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | -0.128 |  |
| 2026-10-15 08:04:39 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-15 08:04:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:03:37 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:03:33 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:03:32 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:03:31 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 08:03:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-10-15 08:03:29 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 08:03:19 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.179 |  |
| 2026-10-15 08:03:16 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-15 08:03:03 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:03:01 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:02:50 | Hanwella (Kelani Ganga) | 4.95 | 🟢 Normal | -0.041 |  |
| 2026-10-15 08:02:41 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.020 |  |
| 2026-10-15 08:02:08 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-10-15 08:02:07 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 08:02:05 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 08:01:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.098 |  |
| 2026-10-15 08:01:49 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.049 |  |
| 2026-10-15 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:01:09 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:01:07 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 08:01:03 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:00:03 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 08:02:05 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 08:03:16 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-15 08:06:21 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.019 |  |
| 2026-10-15 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.020 |  |
| 2026-10-15 08:08:31 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-15 08:03:31 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 08:04:39 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-15 08:08:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 08:03:29 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 08:01:07 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 08:02:41 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 08:11:42 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-15 08:02:07 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 08:07:48 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-15 08:03:37 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:01:09 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:09:52 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:07:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:03:33 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:03:03 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:10:10 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:04:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:03:32 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:01:09 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:05:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-15 08:07:04 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-10-15 08:09:57 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-10-15 08:05:52 | Rathnapura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.033 |  |
| 2026-10-15 08:03:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-10-15 08:02:50 | Hanwella (Kelani Ganga) | 4.95 | 🟢 Normal | -0.041 |  |
| 2026-10-15 08:01:49 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.049 |  |
| 2026-10-15 08:00:03 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.052 |  |
| 2026-10-15 08:02:08 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.071 |  |
| 2026-10-15 07:12:11 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.078 |  |
| 2026-10-15 08:01:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.098 |  |
| 2026-10-15 08:05:38 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | -0.128 |  |
| 2026-10-15 08:03:19 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.179 |  |
| 2026-10-15 08:06:28 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)