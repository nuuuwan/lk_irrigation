# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_01:57:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 01:57:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 01:56:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 01:33:43 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.007 |  |
| 2026-04-28 01:17:25 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.065 |  |
| 2026-04-28 01:16:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:12:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:12:42 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.018 |  |
| 2026-04-28 01:12:41 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -18.000 |  |
| 2026-04-28 01:12:39 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -18.000 |  |
| 2026-04-28 01:12:23 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:07:43 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.200 |  |
| 2026-04-28 01:07:29 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:07:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-28 01:07:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.080 |  |
| 2026-04-28 01:06:49 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 01:06:42 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:05:56 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:05:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 01:57:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 3.857 | 🔺 Rising |
| 2026-04-28 01:01:58 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-28 01:04:35 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-28 01:02:47 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-28 00:03:47 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 01:01:09 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 01:06:49 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 01:04:20 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-28 01:04:51 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:07:29 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:05:56 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 01:05:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:12:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:02:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:01:34 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:42 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:04:11 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:01:57 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:16:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:12:23 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:03:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:33:43 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.007 |  |
| 2026-04-27 23:07:50 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-04-28 01:07:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-28 01:01:28 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-28 01:12:42 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.018 |  |
| 2026-04-28 01:04:19 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-04-28 01:17:25 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.065 |  |
| 2026-04-28 01:03:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-04-28 01:03:26 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.077 |  |
| 2026-04-28 01:07:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.080 |  |
| 2026-04-28 01:04:23 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.127 |  |
| 2026-04-28 01:07:43 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.200 |  |
| 2026-04-28 01:12:41 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)