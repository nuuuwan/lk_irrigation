# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_02:21:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 02:21:16 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-02-06 02:15:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.032 |  |
| 2026-02-06 02:11:28 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 02:10:36 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 02:10:27 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:07:35 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:06:55 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:06:09 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:05:50 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:05:30 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 02:04:39 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-06 02:03:45 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 02:03:43 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-02-06 02:03:12 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.147 |  |
| 2026-02-06 02:03:07 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.371 |  |
| 2026-02-06 02:03:07 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:03:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:02:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:02:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -1.714 |  |
| 2026-02-06 02:02:42 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-06 02:02:22 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -1.714 |  |
| 2026-02-06 02:02:13 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-02-06 02:01:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-06 02:01:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:00:45 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 23:13:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-06 02:01:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-06 02:02:42 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 02:05:30 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 02:03:45 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 02:11:28 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 02:10:36 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 01:34:28 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.005 |  |
| 2026-02-06 02:01:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:03:07 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 01:05:26 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:03:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:07:35 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 00:04:22 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:02:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-06 01:54:14 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:06:55 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:05:50 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:06:09 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-06 02:10:27 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-06 01:41:55 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.006 |  |
| 2026-02-06 00:04:48 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-02-06 02:04:39 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-06 01:07:26 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-02-06 02:02:13 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-02-06 02:15:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.032 |  |
| 2026-02-06 02:21:16 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-06 02:03:43 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 02:03:12 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.147 |  |
| 2026-02-06 02:03:07 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.371 |  |
| 2026-02-06 02:02:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -1.714 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)