# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_19:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 19:18:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-02-22 19:15:26 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-22 19:11:41 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-02-22 19:11:05 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-02-22 19:10:53 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | -0.035 |  |
| 2026-02-22 19:09:40 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.084 |  |
| 2026-02-22 19:08:41 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-22 19:08:22 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.065 |  |
| 2026-02-22 19:07:39 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-02-22 19:06:45 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.391 |  |
| 2026-02-22 19:06:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-02-22 19:06:17 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-22 19:06:13 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.178 |  |
| 2026-02-22 19:06:04 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.047 |  |
| 2026-02-22 19:05:59 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-22 19:05:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.028 |  |
| 2026-02-22 19:05:11 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:05:01 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:04:59 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.097 |  |
| 2026-02-22 19:04:40 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-02-22 19:04:01 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-02-22 19:03:41 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.391 |  |
| 2026-02-22 19:03:35 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.135 |  |
| 2026-02-22 19:03:33 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:03:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:03:04 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:02:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-22 19:02:27 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.073 |  |
| 2026-02-22 19:02:15 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:34 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-22 19:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.01 | 🟡 Alert | -0.035 |  |
| 2026-02-22 19:00:48 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-02-22 19:00:44 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.000 |  |
| 2026-02-22 18:57:28 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.000 |  |
| 2026-02-22 18:57:12 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 19:00:44 | Manampitiya (Mahaweli Ganga) | 3.54 | 🟡 Alert | 0.000 |  |
| 2026-02-22 19:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.01 | 🟡 Alert | -0.035 |  |
| 2026-02-22 19:01:30 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 19:05:59 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 19:08:41 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-22 19:15:26 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-22 19:05:01 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:02:15 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:03:04 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:05:11 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:03:33 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:01:34 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-22 19:06:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-02-22 19:02:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-22 18:03:35 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-22 19:07:39 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-02-22 19:06:17 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-22 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-22 19:00:48 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-02-22 18:57:12 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-02-22 19:05:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.028 |  |
| 2026-02-22 19:04:40 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-02-22 19:10:53 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | -0.035 |  |
| 2026-02-22 19:04:01 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-02-22 19:11:41 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-02-22 19:11:05 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-02-22 19:06:04 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.047 |  |
| 2026-02-22 19:08:22 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.065 |  |
| 2026-02-22 19:02:27 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.073 |  |
| 2026-02-22 19:09:40 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.084 |  |
| 2026-02-22 19:18:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-02-22 19:04:59 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.097 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 19:03:35 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.135 |  |
| 2026-02-22 19:06:13 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.178 |  |
| 2026-02-22 19:06:45 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.391 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)