# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_09:23:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 09:23:46 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 09:12:36 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:10:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:09:46 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:08:31 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-18 09:07:17 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:06:48 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-02-18 09:06:25 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-18 09:05:33 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:05:28 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:05:16 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:04:47 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-18 09:04:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 09:04:14 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:04:03 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.083 |  |
| 2026-02-18 09:03:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.163 |  |
| 2026-02-18 09:03:46 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.037 |  |
| 2026-02-18 09:03:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:03:37 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 09:06:48 | Padiyathalawa (Maduru Oya) | 1.88 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-02-18 09:03:06 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-02-18 09:06:25 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-18 09:03:09 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 09:01:17 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-18 09:04:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 09:23:46 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 09:00:29 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 08:03:54 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:01:21 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:05:16 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:00:48 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:01:32 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:03:37 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:03:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:02:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:07:17 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:00:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:02:32 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:04:14 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:12:36 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:02:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:03:09 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:10:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:09:46 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:05:33 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 08:01:03 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-18 09:04:47 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-18 09:02:53 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-18 09:01:33 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-18 09:01:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-18 09:03:46 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.037 |  |
| 2026-02-18 09:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-02-18 09:01:26 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.041 |  |
| 2026-02-18 09:08:31 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.059 |  |
| 2026-02-18 09:04:03 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.083 |  |
| 2026-02-18 09:03:01 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.089 |  |
| 2026-02-18 09:03:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)