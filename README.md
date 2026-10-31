# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_09:08:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 09:08:34 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:08:21 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.047 |  |
| 2026-10-31 09:07:46 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:07:43 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:07:21 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:06:45 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.093 |  |
| 2026-10-31 09:06:38 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-31 09:06:17 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:05:48 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-10-31 09:05:01 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.043 |  |
| 2026-10-31 09:04:54 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:04:16 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:04:14 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 09:03:52 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 09:03:27 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.095 |  |
| 2026-10-31 09:03:26 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-31 09:03:19 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.070 |  |
| 2026-10-31 09:03:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-10-31 09:02:48 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:42 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:36 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-31 09:02:30 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:02:27 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:26 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-31 09:02:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:51 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.030 |  |
| 2026-10-31 09:01:43 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2026-10-31 09:01:38 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:36 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 09:01:35 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.094 |  |
| 2026-10-31 09:01:34 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:22 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:00:40 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.151 |  |
| 2026-10-31 09:00:25 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.000 |  |
| 2026-10-31 09:00:20 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:00:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 09:00:25 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | 0.000 |  |
| 2026-10-31 09:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.070 |  |
| 2026-10-31 09:04:14 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 09:03:52 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 09:03:26 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-31 09:02:26 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-31 09:01:36 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 09:00:20 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:38 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:00:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:06:17 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:34 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:02:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:07:43 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:07:46 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:08:34 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:07:21 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 09:03:19 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:04:54 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:02:30 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:04:16 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:02:36 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-31 09:06:38 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-31 09:01:22 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:48 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:27 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:42 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:01:51 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.030 |  |
| 2026-10-31 09:05:01 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.043 |  |
| 2026-10-31 09:08:21 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.047 |  |
| 2026-10-31 09:05:48 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.050 |  |
| 2026-10-31 08:01:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.066 |  |
| 2026-10-31 09:01:43 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
| 2026-10-31 09:06:45 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.093 |  |
| 2026-10-31 09:01:35 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.094 |  |
| 2026-10-31 09:03:27 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.095 |  |
| 2026-10-31 09:03:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-10-31 09:00:40 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)