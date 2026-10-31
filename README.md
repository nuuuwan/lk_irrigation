# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_09:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-10-31 08:04:10 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-31 09:03:26 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-31 09:02:26 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-31 09:01:36 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 09:00:20 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:38 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:00:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:00:23 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:03:03 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:02:31 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:06:25 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.000 |  |
| 2026-10-31 08:05:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:01:34 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:02:09 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 09:03:19 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:02:30 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-10-31 08:03:34 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-31 09:02:36 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-31 08:06:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-10-31 08:05:53 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-10-31 09:01:22 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:48 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:27 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:02:42 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-10-31 09:01:51 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.030 |  |
| 2026-10-31 08:04:18 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-10-31 08:08:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:01:55 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.040 |  |
| 2026-10-31 08:03:51 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-10-31 08:02:21 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.060 |  |
| 2026-10-31 08:01:43 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.066 |  |
| 2026-10-31 09:01:43 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.073 |  |
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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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