# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_23:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 23:14:58 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-01-10 23:14:40 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 23:08:34 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:07:56 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.119 |  |
| 2026-01-10 23:07:46 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:07:05 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 23:06:52 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:06:45 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:06:30 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:05:58 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 23:05:29 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.120 |  |
| 2026-01-10 23:04:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:04:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:04:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 23:03:54 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-10 23:03:52 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-10 23:03:39 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:03:38 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:03:15 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:03:10 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:02:53 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:02:43 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 23:01:53 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:41 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-01-10 23:01:21 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:18 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:18 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:14 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:00:18 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-01-10 23:00:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:22:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 22:20:54 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 23:14:58 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-01-10 23:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 23:04:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 23:07:05 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 23:05:58 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 23:03:54 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-10 23:14:40 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 23:04:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:18 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:21 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:06:45 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:17:18 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:06:30 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:03:39 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:53 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:06:26 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:08:34 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:41 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 22:14:20 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:06:52 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:02:43 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:01:18 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:03:38 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-10 23:02:53 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:07:46 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:03:10 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:03:15 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-10 23:04:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 23:03:52 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-10 23:00:18 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-01-10 23:01:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-01-10 23:07:56 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.119 |  |
| 2026-01-10 23:05:29 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)