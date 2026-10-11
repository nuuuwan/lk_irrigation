# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_07:15:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,741 measurements** from **39** stations.
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
| 2026-10-11 07:15:57 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.058 |  |
| 2026-10-11 07:15:04 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:13:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-11 07:11:24 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:10:26 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-11 07:10:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-11 07:09:31 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.108 |  |
| 2026-10-11 07:09:24 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.056 |  |
| 2026-10-11 07:09:10 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-11 07:08:52 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.009 |  |
| 2026-10-11 07:08:38 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.046 |  |
| 2026-10-11 07:07:15 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:07:10 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.145 |  |
| 2026-10-11 07:06:53 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-10-11 07:06:08 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-11 07:05:52 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.143 |  |
| 2026-10-11 07:04:57 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:51 | Badalgama (Maha Oya) | 4.05 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:04:42 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:34 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-11 07:04:09 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:05 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-10-11 07:03:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:03:31 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.045 |  |
| 2026-10-11 07:03:24 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.172 |  |
| 2026-10-11 07:03:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:03:00 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 07:02:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.157 |  |
| 2026-10-11 07:01:55 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:01:40 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:01:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:00:53 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 07:00:53 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-11 07:00:42 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-11 07:00:42 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-10-11 07:00:26 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 07:00:42 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-10-11 07:09:10 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-11 07:10:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-11 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-11 07:06:08 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-11 07:00:53 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 07:03:00 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 07:13:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-11 07:01:40 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:01:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:15:04 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:57 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:03:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:07:15 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:03:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:09 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:10:26 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:04:42 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:06:53 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-10-11 07:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-11 07:08:52 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.009 |  |
| 2026-10-11 06:00:48 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.016 |  |
| 2026-10-11 07:04:34 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-10-11 07:01:55 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:00:26 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:04:51 | Badalgama (Maha Oya) | 4.05 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:00:53 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:11:24 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-11 07:00:42 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-11 07:03:31 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.045 |  |
| 2026-10-11 07:08:38 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.046 |  |
| 2026-10-11 07:04:05 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-10-11 07:09:24 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.056 |  |
| 2026-10-11 07:15:57 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.058 |  |
| 2026-10-11 07:09:31 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.108 |  |
| 2026-10-11 07:05:52 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.143 |  |
| 2026-10-11 07:07:10 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.145 |  |
| 2026-10-11 07:02:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.157 |  |
| 2026-10-11 07:03:24 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)