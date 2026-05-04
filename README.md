# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_00:45:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 00:45:51 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.014 |  |
| 2026-05-05 00:12:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:12:24 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-05-05 00:10:02 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 00:09:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 00:06:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-05-05 00:02:39 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 1.022 | 🔺 Rising |
| 2026-05-05 00:03:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-05 00:01:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-05 00:01:28 | Yaka Wewa (Ma Oya) | 1.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-05 00:04:50 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 00:10:02 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:34 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:01:47 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:05:32 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:02:07 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:01:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:05:00 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:03:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:12:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:01:37 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:02:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:03:08 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:03:51 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:10:32 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-05 00:05:10 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-05-05 00:07:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-05 00:02:52 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-05 00:45:51 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.014 |  |
| 2026-05-05 00:07:16 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-05 00:04:57 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-05-05 00:12:24 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-05-05 00:06:07 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-05-04 23:07:25 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-05-05 00:02:25 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.062 |  |
| 2026-05-05 00:04:23 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)