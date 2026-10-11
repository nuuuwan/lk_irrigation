# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_03:29:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,493 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 03:29:31 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.004 |  |
| 2026-10-12 03:21:15 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.017 |  |
| 2026-10-12 03:11:06 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 03:09:31 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -108.000 |  |
| 2026-10-12 03:09:30 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -108.000 |  |
| 2026-10-12 03:08:57 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.029 |  |
| 2026-10-12 03:08:24 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-12 03:08:22 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-10-12 03:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:07:58 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 03:07:25 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-12 03:06:42 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -18.000 |  |
| 2026-10-12 03:06:40 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -18.000 |  |
| 2026-10-12 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:38 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:36 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:16 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 03:06:00 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-12 03:05:52 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -14.727 |  |
| 2026-10-12 03:05:50 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 03:05:08 | Thawalama (Gin Ganga) | 3.68 | 🟢 Normal | -14.727 |  |
| 2026-10-12 03:04:33 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-10-12 03:04:17 | Magura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.161 |  |
| 2026-10-12 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-12 03:04:00 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.142 |  |
| 2026-10-12 03:03:41 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 03:03:30 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-12 03:03:07 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-12 03:02:54 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:48 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:47 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 03:02:43 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:34 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:09 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.071 |  |
| 2026-10-12 03:01:11 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.067 |  |
| 2026-10-12 03:00:44 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 03:00:12 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 03:08:24 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-12 03:07:25 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-12 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-12 03:02:47 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 03:07:58 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 03:03:30 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-12 03:03:07 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-12 03:03:41 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 03:11:06 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 02:00:09 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 03:06:16 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 02:35:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-12 03:00:44 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 03:05:50 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 02:04:14 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:43 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:54 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:48 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 02:02:00 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:02:34 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:29:31 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.004 |  |
| 2026-10-12 03:04:33 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 03:21:15 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.017 |  |
| 2026-10-12 03:00:12 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-10-12 03:08:57 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.029 |  |
| 2026-10-12 03:06:00 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-12 03:01:11 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.067 |  |
| 2026-10-12 03:08:22 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-10-12 03:02:09 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.071 |  |
| 2026-10-12 03:04:00 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.142 |  |
| 2026-10-12 03:04:17 | Magura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.161 |  |
| 2026-10-12 03:05:52 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -14.727 |  |
| 2026-10-12 03:06:42 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -18.000 |  |
| 2026-10-12 03:09:31 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)