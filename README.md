# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_10:26:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 10:26:44 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:22:27 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:14:36 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:12:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.061 |  |
| 2026-02-06 10:11:00 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:09:51 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:09:04 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:08:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:07:26 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.014 |  |
| 2026-02-06 10:06:46 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.056 |  |
| 2026-02-06 10:05:32 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:05:20 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-06 10:05:13 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:05:03 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-02-06 10:04:54 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-06 10:04:48 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:04:24 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-06 10:04:20 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:47 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-06 10:03:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 10:03:23 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:17 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 10:03:15 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:10 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.062 |  |
| 2026-02-06 10:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 10:01:59 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -72.000 |  |
| 2026-02-06 10:01:57 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -72.000 |  |
| 2026-02-06 10:01:53 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.154 |  |
| 2026-02-06 10:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:01:34 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:00:58 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:00:55 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-06 10:00:39 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 10:05:03 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-02-06 10:03:46 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 10:03:17 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 10:00:55 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-06 10:03:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 10:05:20 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-06 09:05:51 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 10:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 10:00:58 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:06:46 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:04:48 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:11:00 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:05:13 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:09:04 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:03:23 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:08:17 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:14:36 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:26:44 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:02:26 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:22:27 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 10:09:51 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:01:34 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:05:32 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-06 10:00:39 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-02-06 10:07:26 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.014 |  |
| 2026-02-06 10:04:24 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-06 10:04:54 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-02-06 10:06:37 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.056 |  |
| 2026-02-06 10:12:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.061 |  |
| 2026-02-06 10:03:10 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.062 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 10:01:53 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.154 |  |
| 2026-02-06 10:01:59 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)