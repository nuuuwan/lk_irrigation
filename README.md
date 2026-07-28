# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_12:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,496 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 12:14:58 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:12:23 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-07-28 12:11:07 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:09:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:09:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:08:27 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-07-28 12:07:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-07-28 12:06:25 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:06:22 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 12:06:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:05:35 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2026-07-28 12:05:29 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 12:05:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:04:29 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:34 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:17 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.042 |  |
| 2026-07-28 12:03:16 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-07-28 12:03:14 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:54 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-07-28 12:02:46 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 12:02:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:26 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-28 12:02:23 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:02:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:33 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 12:01:32 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.112 |  |
| 2026-07-28 12:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:11 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:07 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:00:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-07-28 12:00:45 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:00:40 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:00:31 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 12:00:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-07-28 12:07:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-07-28 12:06:22 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 12:01:33 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-28 12:02:46 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 12:05:29 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 12:02:26 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-28 12:03:34 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:00:40 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:14 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:00:31 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:04:29 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:11:07 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:16 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:09:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:14:58 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:02 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:11 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:06:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:05:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:09:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:01:07 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:03:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:12:23 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-07-28 12:06:25 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:02:23 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:00:45 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-28 12:05:35 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2026-07-28 12:08:27 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-07-28 12:02:54 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-07-28 12:03:17 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.042 |  |
| 2026-07-28 12:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-07-28 12:01:32 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)