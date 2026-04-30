# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_07:15:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,882 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 07:15:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.050 |  |
| 2026-04-30 07:13:17 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-04-30 07:12:45 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:12:34 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:09:45 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.075 |  |
| 2026-04-30 07:08:56 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:08:25 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.038 |  |
| 2026-04-30 07:08:13 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:06:11 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:06:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:05:18 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.022 |  |
| 2026-04-30 07:05:09 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:05:01 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-30 07:04:59 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:04:48 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:04:29 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.067 |  |
| 2026-04-30 07:03:55 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.019 |  |
| 2026-04-30 07:03:54 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 07:03:23 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:03:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 07:03:17 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-04-30 07:03:14 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:03:12 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-30 07:02:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.031 |  |
| 2026-04-30 07:02:48 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-04-30 07:02:31 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-30 07:02:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:02:21 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-04-30 07:02:20 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 07:02:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.069 |  |
| 2026-04-30 07:01:46 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-30 07:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-30 07:00:44 | Thanthirimale (Malwathu Oya) | 2.54 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-30 07:00:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-30 07:00:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:37:52 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-30 06:36:36 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 07:02:31 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-30 07:00:44 | Thanthirimale (Malwathu Oya) | 2.54 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-30 07:05:01 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-30 07:01:46 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-30 07:03:54 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 07:02:20 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 07:03:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 06:05:55 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 07:00:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:08:13 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:12:45 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:08:56 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:06:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:04:48 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:06:11 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 06:02:33 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:12:34 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:04:59 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:02:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 07:13:17 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-04-30 07:03:12 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-30 07:03:55 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.019 |  |
| 2026-04-30 07:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-30 07:05:18 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.022 |  |
| 2026-04-30 06:07:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-04-30 07:02:48 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-04-30 07:02:21 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.031 |  |
| 2026-04-30 07:02:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.031 |  |
| 2026-04-30 06:01:24 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-04-30 07:08:25 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.038 |  |
| 2026-04-30 07:03:14 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:05:09 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:03:23 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.039 |  |
| 2026-04-30 07:03:17 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-04-30 07:00:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-04-30 07:15:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.050 |  |
| 2026-04-30 07:04:29 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.067 |  |
| 2026-04-30 07:02:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.069 |  |
| 2026-04-30 07:09:45 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)