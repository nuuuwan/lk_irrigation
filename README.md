# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_15:07:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,566 measurements** from **39** stations.
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
| 2026-10-06 15:07:13 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 15:06:34 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-06 15:06:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:06:04 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.091 |  |
| 2026-10-06 15:05:49 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.088 |  |
| 2026-10-06 15:05:31 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:05:08 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.045 |  |
| 2026-10-06 15:04:55 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:04:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-06 15:04:44 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:26 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.079 |  |
| 2026-10-06 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.048 |  |
| 2026-10-06 15:04:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.068 |  |
| 2026-10-06 15:03:44 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 15:03:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:03:16 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.059 |  |
| 2026-10-06 15:03:15 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-10-06 15:03:14 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:03:12 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:03:09 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.102 |  |
| 2026-10-06 15:03:07 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:02:55 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-10-06 15:02:44 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:02:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:02:36 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.030 |  |
| 2026-10-06 15:02:16 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.032 |  |
| 2026-10-06 15:02:06 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:01:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:01:23 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-10-06 15:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:01:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:01:16 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-10-06 15:01:10 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:01:08 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.153 |  |
| 2026-10-06 15:01:05 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:00:31 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 15:03:44 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 15:07:13 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 15:01:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:01:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:06:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:00:31 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:02:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:02:44 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:05:31 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:03:12 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:44 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:02:06 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:01:05 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 15:04:55 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:03:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:03:14 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-06 15:03:15 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-10-06 15:01:16 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-10-06 15:04:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-06 15:02:36 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.030 |  |
| 2026-10-06 15:01:23 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-10-06 15:02:55 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-10-06 15:02:16 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.032 |  |
| 2026-10-06 15:01:10 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:03:07 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.039 |  |
| 2026-10-06 15:06:34 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-10-06 15:05:08 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.045 |  |
| 2026-10-06 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.048 |  |
| 2026-10-06 15:03:16 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.059 |  |
| 2026-10-06 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.068 |  |
| 2026-10-06 15:04:26 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.079 |  |
| 2026-10-06 15:05:49 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.088 |  |
| 2026-10-06 15:06:04 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.091 |  |
| 2026-10-06 15:03:09 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.102 |  |
| 2026-10-06 15:01:08 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)