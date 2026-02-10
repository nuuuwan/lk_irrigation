# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_14:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 14:18:49 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.016 |  |
| 2026-02-10 14:11:51 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:09:35 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.036 |  |
| 2026-02-10 14:08:46 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:07:46 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-02-10 14:07:05 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-10 14:06:40 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:06:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-02-10 14:06:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:06:20 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:05:22 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:04:56 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:04:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 14:03:54 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:28 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:16 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:03:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-10 14:02:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:48 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:35 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:34 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:28 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-10 14:02:25 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:15 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-02-10 14:02:06 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:06 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-02-10 14:01:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:01:36 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:01:30 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.051 |  |
| 2026-02-10 14:01:16 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-10 14:01:14 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 14:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:00:37 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:00:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:40:04 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 14:07:05 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-10 14:03:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-10 14:02:28 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-10 14:01:14 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 14:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 14:02:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:25 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:54 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:48 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:05:22 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:06:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:06 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:39 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:34 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:06:20 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:28 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:00:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:01:36 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:00:37 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:02:35 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:01:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:06:40 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:03:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:04:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 14:08:46 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:04:56 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:11:51 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:03:16 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-10 14:06:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-02-10 14:01:16 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-10 14:02:06 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-02-10 13:40:04 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.013 |  |
| 2026-02-10 14:18:49 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.016 |  |
| 2026-02-10 14:07:46 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-02-10 14:02:15 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-02-10 14:09:35 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.036 |  |
| 2026-02-10 14:01:30 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)