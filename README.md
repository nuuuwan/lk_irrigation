# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_23:00:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 23:00:43 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-11 22:34:30 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.007 |  |
| 2026-05-11 22:14:05 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.018 |  |
| 2026-05-11 22:12:33 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 22:11:00 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:09:50 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:09:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 23:00:43 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-11 22:03:00 | Moragaswewa (Deduru Oya) | 2.54 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-11 21:01:26 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 22:02:10 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 22:06:52 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-11 22:03:37 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 22:02:33 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-11 22:04:36 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 22:02:31 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 22:01:07 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 22:02:42 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 22:04:08 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 22:12:33 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 22:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:01:45 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:00:17 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:11:00 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:04:05 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:09:50 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:00:09 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:02:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:07:10 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:09:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 22:34:30 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.007 |  |
| 2026-05-11 22:14:05 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.018 |  |
| 2026-05-11 22:06:36 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-05-11 22:05:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-11 22:02:37 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.039 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-11 22:04:50 | Katharagama (Menik Ganga) | 2.34 | 🟢 Normal | -0.050 |  |
| 2026-05-11 22:04:23 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-11 22:00:38 | Wellawaya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.099 |  |
| 2026-05-11 22:03:30 | Siyambalanduwa (Heda Oya) | 2.64 | 🟢 Normal | -0.113 |  |
| 2026-05-11 22:03:31 | Thaldena (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.150 |  |
| 2026-05-11 22:02:21 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.230 |  |
| 2026-05-11 22:02:09 | Nakkala (Kumbukkan Oya) | 1.85 | 🟢 Normal | -0.291 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)