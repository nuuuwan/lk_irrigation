# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_09:08:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 09:08:48 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 09:08:35 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.055 |  |
| 2026-10-24 09:07:49 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-10-24 09:07:45 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:07:39 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:06:54 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:06:14 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-24 09:06:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-10-24 09:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:05:08 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:04:57 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:04:42 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-10-24 09:04:17 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.070 |  |
| 2026-10-24 09:04:03 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:04:01 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 09:03:56 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:32 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-10-24 09:03:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:03:31 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:03:18 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:03:06 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.040 |  |
| 2026-10-24 09:03:05 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:03 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-10-24 09:02:57 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-24 09:02:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 09:02:53 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.101 |  |
| 2026-10-24 09:02:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:02:50 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.043 |  |
| 2026-10-24 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.030 |  |
| 2026-10-24 09:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-24 09:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-10-24 09:01:48 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.043 |  |
| 2026-10-24 09:01:24 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.080 |  |
| 2026-10-24 09:01:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:01:18 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-10-24 09:01:17 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 09:00:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 09:02:57 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-24 09:08:48 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 09:06:14 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-24 09:04:01 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 09:01:17 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 09:02:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 09:01:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:07:39 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:03:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:06:54 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-24 09:06:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-10-24 09:05:08 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:03:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:04:57 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:00:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:04:03 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-24 09:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-10-24 09:07:49 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-10-24 09:07:45 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:05 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:56 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:02:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:18 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-24 09:03:32 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-10-24 09:03:03 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 09:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-10-24 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.030 |  |
| 2026-10-24 09:01:18 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-10-24 09:03:06 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.040 |  |
| 2026-10-24 09:04:42 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-10-24 09:01:48 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.043 |  |
| 2026-10-24 09:02:50 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.043 |  |
| 2026-10-24 09:08:35 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.055 |  |
| 2026-10-24 08:02:46 | Moragaswewa (Deduru Oya) | 3.33 | 🟢 Normal | -0.068 |  |
| 2026-10-24 09:04:17 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.070 |  |
| 2026-10-24 09:01:24 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.080 |  |
| 2026-10-24 09:02:53 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)