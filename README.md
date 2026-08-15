# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_06:31:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 06:31:41 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.001 |  |
| 2026-08-15 06:13:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:08:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:08:53 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-15 06:07:57 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 06:07:44 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-15 06:06:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 06:05:56 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-15 06:05:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:05:31 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 06:04:36 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.009 |  |
| 2026-08-15 06:04:34 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-15 06:04:26 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-08-15 06:03:59 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.080 |  |
| 2026-08-15 06:03:56 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -9.474 |  |
| 2026-08-15 06:03:37 | Deraniyagala (Kelani Ganga) | 1.91 | 🟢 Normal | -9.474 |  |
| 2026-08-15 06:03:29 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:08 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.144 |  |
| 2026-08-15 06:03:00 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:38 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:26 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-08-15 06:02:20 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-08-15 06:02:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:11 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:08 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-15 06:01:56 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:46 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:37 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.033 |  |
| 2026-08-15 06:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 1.004 | 🔺 Rising |
| 2026-08-15 06:01:20 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 06:01:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-08-15 06:01:09 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-15 06:00:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:00:37 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-15 06:00:31 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:56:49 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 06:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 1.004 | 🔺 Rising |
| 2026-08-15 06:04:26 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-08-15 06:02:08 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-15 06:08:53 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-15 06:01:09 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-15 06:06:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 06:05:56 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-15 06:04:34 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-15 06:01:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 06:05:31 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 06:07:44 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-15 06:07:57 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 06:03:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:46 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:20 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:00:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:00 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:13:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:38 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:08:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:01:56 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:05:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:03:29 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:02:11 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 06:31:41 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.001 |  |
| 2026-08-15 06:04:36 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.009 |  |
| 2026-08-15 06:00:37 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-15 06:02:26 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-08-15 06:02:20 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-08-15 06:01:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-08-15 06:01:37 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.033 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-15 06:03:59 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.080 |  |
| 2026-08-15 06:03:08 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.144 |  |
| 2026-08-15 06:03:56 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -9.474 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)