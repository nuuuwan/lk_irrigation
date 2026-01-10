# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_08:26:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,616 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 08:26:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:19:39 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:19:26 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-10 08:16:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.017 |  |
| 2026-01-10 08:16:20 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-01-10 08:16:10 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:10:49 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 08:09:45 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 08:08:28 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-10 08:07:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-10 08:07:10 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.077 |  |
| 2026-01-10 08:06:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:06:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-01-10 08:05:36 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:05:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:05:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-10 08:04:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:04:47 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:04:37 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:04:06 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:04:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:03:45 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-10 08:03:13 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:53 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:31 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:19 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-10 08:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:03 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:01:31 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.048 |  |
| 2026-01-10 08:01:24 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 08:01:23 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-01-10 08:00:36 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-10 08:00:31 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-10 08:00:25 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.004 |  |
| 2026-01-10 07:56:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 08:03:45 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-10 08:00:31 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-10 08:01:24 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 08:05:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-10 08:00:36 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-10 08:10:49 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 08:02:19 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 08:04:49 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:31 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:02:03 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:04:47 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:05:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 08:09:45 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 08:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:53 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:23 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:16:10 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:03:13 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:01:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:04:37 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:04:06 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:06:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:26:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 08:00:25 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.004 |  |
| 2026-01-10 08:16:20 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-01-10 08:19:26 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-10 08:04:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:19:39 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:05:36 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-10 08:08:28 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-10 08:16:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.017 |  |
| 2026-01-10 07:09:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.018 |  |
| 2026-01-10 08:07:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-10 08:01:31 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.048 |  |
| 2026-01-10 08:01:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-01-10 08:06:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-01-10 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-10 08:07:10 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)