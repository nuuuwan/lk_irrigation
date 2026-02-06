# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_11:30:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,549 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 11:30:08 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:23:15 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:13:20 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:10:01 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:08:14 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.195 |  |
| 2026-02-06 11:07:53 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:07:42 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:06:08 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 636.000 | 🔺 Rising |
| 2026-02-06 11:06:05 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | 636.000 | 🔺 Rising |
| 2026-02-06 11:06:04 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 11:04:47 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:04:34 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 11:04:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:03:55 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 11:03:33 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:03:22 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.049 |  |
| 2026-02-06 11:02:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.030 |  |
| 2026-02-06 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:41 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:41 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-06 11:02:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 11:02:21 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-06 11:02:08 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:04 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.051 |  |
| 2026-02-06 11:02:02 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-06 11:01:47 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:46 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:43 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:21 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-02-06 11:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-06 11:01:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2026-02-06 11:00:59 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-06 11:00:40 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:00:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 11:06:08 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 636.000 | 🔺 Rising |
| 2026-02-06 11:02:02 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 11:04:34 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 11:02:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-06 11:02:21 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-06 11:00:59 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-06 11:03:55 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 11:06:04 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 11:01:43 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:10:01 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:47 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:46 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:03:33 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:13:20 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:41 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:00:40 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:04:47 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:00:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:04:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:07:53 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:07:42 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:30:08 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:02:08 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:26:44 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:23:15 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-06 11:01:21 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-02-06 11:01:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2026-02-06 11:02:41 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-06 11:02:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.030 |  |
| 2026-02-06 11:03:22 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.049 |  |
| 2026-02-06 11:02:04 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.051 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 11:08:14 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)