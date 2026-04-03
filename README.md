# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_11:23:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,966 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 11:23:10 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.052 |  |
| 2026-04-03 11:19:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.040 |  |
| 2026-04-03 11:16:21 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-04-03 11:12:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:11:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:10:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-04-03 11:08:54 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:08:46 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.071 |  |
| 2026-04-03 11:08:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:08:30 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:08:05 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 11:07:46 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-04-03 11:07:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-03 11:07:32 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:06:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:05:06 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:04:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:04:58 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-03 11:04:41 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.072 |  |
| 2026-04-03 11:04:24 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:46 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-03 11:03:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:17 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 11:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:02:47 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-03 11:02:19 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:02:10 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-03 11:02:08 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 11:02:07 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-03 11:01:59 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-03 11:01:30 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.033 |  |
| 2026-04-03 11:01:27 | Thanthirimale (Malwathu Oya) | 2.91 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-03 11:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:01:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:01:12 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-04-03 11:00:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 10:23:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-03 11:07:45 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-03 11:01:27 | Thanthirimale (Malwathu Oya) | 2.91 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-03 11:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-03 11:04:58 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-03 11:02:10 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-03 11:02:08 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 11:08:05 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 11:08:54 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:02:19 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:17 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:00:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:04:58 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:11:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:12:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:07:32 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:05:06 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:01:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:04:24 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:06:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:08:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:08:30 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:01:59 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-03 11:02:07 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-03 11:10:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-04-03 11:16:21 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-04-03 11:07:46 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-04-03 11:03:46 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-03 11:02:47 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-04-03 11:01:30 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.033 |  |
| 2026-04-03 11:01:12 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-04-03 11:19:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.040 |  |
| 2026-04-03 11:23:10 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.052 |  |
| 2026-04-03 11:08:46 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.071 |  |
| 2026-04-03 11:04:41 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)