# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_07:35:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,967 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 07:35:02 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-23 07:34:00 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-06-23 07:18:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:12:55 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:11:40 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:11:31 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-06-23 07:09:31 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-23 07:08:55 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | -0.151 |  |
| 2026-06-23 07:08:30 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.091 |  |
| 2026-06-23 07:08:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:07:20 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.096 |  |
| 2026-06-23 07:06:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:06:31 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.071 |  |
| 2026-06-23 07:06:14 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:06:03 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-23 07:05:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-23 07:05:08 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:04:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:04:26 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 07:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-06-23 07:03:45 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.038 |  |
| 2026-06-23 07:03:42 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-23 07:03:08 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 07:03:08 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.218 |  |
| 2026-06-23 07:02:59 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-06-23 07:02:56 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-23 07:02:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:02:21 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-23 07:02:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:01:49 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-23 07:01:47 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:01:13 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 07:01:13 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-23 07:00:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:00:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:00:24 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:00:15 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.082 |  |
| 2026-06-23 07:00:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 07:01:49 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-23 07:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-23 07:00:12 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-23 07:01:13 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-23 07:02:56 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-23 07:02:21 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-23 07:03:42 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-23 07:09:31 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-23 07:03:08 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-23 07:35:02 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-23 07:04:26 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 07:06:03 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-23 07:01:13 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 07:00:24 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:02:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:06:14 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 07:00:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:02:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:11:40 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:12:55 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:04:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:05:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:06:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:00:58 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:18:44 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:08:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:01:47 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:05:08 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 07:02:59 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-06-23 07:03:45 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.038 |  |
| 2026-06-23 07:34:00 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-06-23 07:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-06-23 07:11:31 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.067 |  |
| 2026-06-23 07:06:31 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.071 |  |
| 2026-06-23 07:00:15 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.082 |  |
| 2026-06-23 07:08:30 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.091 |  |
| 2026-06-23 07:07:20 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.096 |  |
| 2026-06-23 07:08:55 | Glencourse (Kelani Ganga) | 13.04 | 🟢 Normal | -0.151 |  |
| 2026-06-23 07:03:08 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)