# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_07:09:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 07:09:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:09:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.239 |  |
| 2026-04-15 07:09:23 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.047 |  |
| 2026-04-15 07:08:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:08:31 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.075 |  |
| 2026-04-15 07:07:56 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 07:07:29 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-15 07:06:57 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:06:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:06:25 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:05:59 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:05:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:05:21 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-15 07:04:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.077 |  |
| 2026-04-15 07:03:55 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:03:28 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:03:24 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:03:24 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-15 07:03:22 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:03:10 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-15 07:02:52 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.052 |  |
| 2026-04-15 07:02:41 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.048 |  |
| 2026-04-15 07:02:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:25 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:18 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:03 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:01:43 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:01:33 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:01:32 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:01:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 07:00:24 | Thanthirimale (Malwathu Oya) | 2.80 | 🟢 Normal | -0.076 |  |
| 2026-04-15 07:00:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-15 06:59:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 06:40:38 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-15 06:19:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 06:04:12 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-15 07:07:29 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-15 07:00:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-15 07:03:24 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-15 07:05:21 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-15 07:03:10 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-15 07:07:56 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 07:05:59 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:06:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:09:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 07:01:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 06:05:59 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 07:08:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 06:59:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:05:44 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:18 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:01:32 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-15 06:12:23 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:06:57 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:03:28 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:02:25 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:09:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:06:25 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:01:43 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:03:24 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:01:33 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-15 06:16:04 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-15 07:03:22 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:02:03 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:03:55 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-15 07:09:23 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.047 |  |
| 2026-04-15 07:02:41 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.048 |  |
| 2026-04-15 07:02:52 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.052 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 07:08:31 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.075 |  |
| 2026-04-15 07:00:24 | Thanthirimale (Malwathu Oya) | 2.80 | 🟢 Normal | -0.076 |  |
| 2026-04-15 07:04:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.077 |  |
| 2026-04-15 07:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)