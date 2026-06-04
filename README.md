# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_20:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 20:07:56 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-04 20:06:53 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 11.613 | 🔺 Rising |
| 2026-06-04 20:06:27 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-04 20:06:10 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 20:05:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:05:20 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 11.613 | 🔺 Rising |
| 2026-06-04 20:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:05:11 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-04 20:05:05 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-04 20:04:38 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 20:04:30 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-04 20:04:30 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:04:15 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |
| 2026-06-04 20:03:45 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:43 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-04 20:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 20:03:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-04 20:03:22 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 20:03:12 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:03:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:02:38 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 20:02:07 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -6.000 |  |
| 2026-06-04 20:01:27 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:09 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-06-04 20:00:52 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -6.000 |  |
| 2026-06-04 20:00:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:50:34 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-04 19:37:21 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.013 |  |
| 2026-06-04 19:17:43 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 20:06:53 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 11.613 | 🔺 Rising |
| 2026-06-04 20:05:05 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-04 20:05:11 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-04 20:07:56 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-04 20:03:43 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-04 20:03:22 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 20:06:27 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-04 20:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 20:02:38 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 19:17:13 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 20:04:38 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 19:06:56 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 20:06:10 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 20:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:03:12 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:04:30 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 20:01:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:02:07 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:13:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:45 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:03:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:05:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:00:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:04:15 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:01:27 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:20 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 20:04:30 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-04 20:03:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-04 19:37:21 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.013 |  |
| 2026-06-04 19:13:07 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.025 |  |
| 2026-06-04 19:06:08 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.055 |  |
| 2026-06-04 20:01:09 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-06-04 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |
| 2026-06-04 20:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -6.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)