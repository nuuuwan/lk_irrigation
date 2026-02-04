# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_04:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 04:13:13 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.121 |  |
| 2026-02-05 04:12:19 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-05 04:11:32 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:08:38 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-02-05 04:08:37 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-02-05 04:07:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:07:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:07:01 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-05 04:05:53 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 04:05:35 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-05 04:05:29 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:04:49 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:03:50 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-05 04:03:48 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.165 |  |
| 2026-02-05 04:03:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-02-05 04:03:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:03:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:02:58 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:02:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:02:08 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-02-05 04:01:46 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:01:45 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:01:43 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-05 04:01:38 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-05 04:01:34 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:01:21 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-05 04:01:06 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-05 04:00:59 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:00:37 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:00:28 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-02-05 04:00:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 03:58:24 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.121 |  |
| 2026-02-05 03:57:59 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.121 |  |
| 2026-02-05 03:57:34 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.121 |  |
| 2026-02-05 03:56:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 03:31:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 04:08:38 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 288.000 | 🔺 Rising |
| 2026-02-05 04:05:35 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 04:07:01 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-05 04:01:06 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-05 04:12:19 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-05 04:00:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 04:05:53 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 04:01:45 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-05 03:03:46 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:04:49 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:13:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:00:37 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:03:15 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:02:58 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:07:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 02:02:02 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:00:59 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:03:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:06:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:11:32 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:07:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:02:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 04:01:46 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 04:03:50 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-05 04:02:08 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.013 |  |
| 2026-02-05 04:01:38 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-05 04:03:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-02-05 04:00:28 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-02-04 18:03:35 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-05 04:13:13 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.121 |  |
| 2026-02-05 04:03:48 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)