# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_08:06:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 08:06:53 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:06:23 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-04-03 08:05:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.139 |  |
| 2026-04-03 08:05:11 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.068 |  |
| 2026-04-03 08:04:52 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:04:38 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-04-03 08:04:34 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:04:09 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-03 08:03:37 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:03:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:03:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-03 08:02:57 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:02:41 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-04-03 08:02:28 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-03 08:02:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 08:01:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:01:15 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.033 |  |
| 2026-04-03 08:01:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:00:58 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.051 |  |
| 2026-04-03 08:00:42 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-03 08:00:33 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-03 08:00:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:00:15 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:31:19 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 07:29:53 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-03 07:26:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.024 |  |
| 2026-04-03 07:24:51 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.033 |  |
| 2026-04-03 07:14:53 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:14:31 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.012 |  |
| 2026-04-03 07:12:58 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 08:02:41 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-04-03 08:00:42 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-03 07:29:53 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-03 08:00:33 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-03 08:04:09 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-03 07:31:19 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 06:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 07:05:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-03 07:07:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 07:01:10 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 08:01:15 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 08:02:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 07:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 08:02:57 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:01:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:50 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:00:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:04:34 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:12:58 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:00:15 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:01:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:03:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:04:52 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:03:37 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:06:53 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 08:02:28 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:08:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-03 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-03 08:06:23 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-04-03 07:26:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.024 |  |
| 2026-04-03 08:04:38 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-04-03 08:03:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-03 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.033 |  |
| 2026-04-03 07:08:33 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-04-03 08:00:58 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.051 |  |
| 2026-04-03 07:02:19 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.051 |  |
| 2026-04-03 08:05:11 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.068 |  |
| 2026-04-03 08:05:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.139 |  |
| 2026-04-03 07:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)