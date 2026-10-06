# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_21:07:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,794 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 21:07:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:07:11 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-06 21:06:51 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.048 |  |
| 2026-10-06 21:06:50 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-10-06 21:06:06 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:06:00 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.028 |  |
| 2026-10-06 21:05:29 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-06 21:05:07 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-06 21:04:53 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.041 |  |
| 2026-10-06 21:04:35 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-06 21:04:06 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:58 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:54 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-06 21:03:38 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-06 21:03:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:29 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.071 |  |
| 2026-10-06 21:03:28 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-06 21:03:09 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:00 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:02:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-06 21:02:53 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 21:02:29 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-06 21:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.005 |  |
| 2026-10-06 21:02:10 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.021 |  |
| 2026-10-06 21:02:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:59 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:55 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 21:01:29 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-06 21:01:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:22 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:18 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 21:02:29 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-06 21:05:29 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-06 21:05:07 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-06 20:07:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 21:01:29 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-06 21:03:38 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-06 21:02:53 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 21:01:55 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 21:07:11 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-06 20:06:06 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 21:03:28 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-06 21:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.005 |  |
| 2026-10-06 20:06:49 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:02:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:04:06 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:28 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:09 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:00 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:06:06 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:59 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:58 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:01:22 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:07:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 21:03:54 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-06 21:04:35 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-06 21:01:18 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 21:06:50 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-10-06 21:02:10 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.021 |  |
| 2026-10-06 21:06:00 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.028 |  |
| 2026-10-06 21:02:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-06 21:04:53 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.041 |  |
| 2026-10-06 21:06:51 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.048 |  |
| 2026-10-06 20:05:30 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.057 |  |
| 2026-10-06 21:03:29 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)