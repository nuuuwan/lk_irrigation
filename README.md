# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_07:00:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:32:19 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:30:32 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-06-10 06:15:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:10:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:09:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 06:01:14 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-06-10 06:07:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-10 06:03:47 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-10 06:03:06 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-10 06:05:02 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-10 06:09:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-10 06:03:25 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 06:08:23 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 06:00:35 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-10 06:03:09 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:02:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:12 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:03:12 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:10:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:30 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:03:40 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:15:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:32:19 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:03:00 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:06:50 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:01:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:07:00 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 06:04:38 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-06-10 06:05:14 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-10 06:05:29 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-10 06:05:59 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-06-10 06:02:16 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-06-10 06:30:32 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-06-10 06:02:21 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.026 |  |
| 2026-06-10 06:02:33 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.031 |  |
| 2026-06-10 06:04:50 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-06-10 06:01:59 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.037 |  |
| 2026-06-10 06:06:24 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.043 |  |
| 2026-06-10 06:02:18 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.060 |  |
| 2026-06-10 06:05:22 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)