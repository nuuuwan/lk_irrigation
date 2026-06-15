# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_20:17:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,324 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 20:17:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:10:01 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:08:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.067 |  |
| 2026-06-15 20:07:34 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-15 20:06:06 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-15 20:05:55 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.032 |  |
| 2026-06-15 20:05:38 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:05:36 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-15 20:05:30 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:05:03 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.033 |  |
| 2026-06-15 20:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:49 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.009 |  |
| 2026-06-15 20:04:47 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:40 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-15 20:04:38 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.020 |  |
| 2026-06-15 20:04:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:20 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.094 |  |
| 2026-06-15 20:03:11 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-06-15 20:03:08 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:03:01 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-15 20:02:59 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:02:51 | Ellagawa (Kalu Ganga) | 5.91 | 🟢 Normal | -0.039 |  |
| 2026-06-15 20:02:50 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:02:41 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-06-15 20:01:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:01:47 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:01:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:01:22 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-06-15 20:01:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:00:45 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:00:42 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:00:15 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 20:01:22 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-06-15 20:03:01 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-15 20:04:40 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-15 19:02:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 20:02:50 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:00:45 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:01:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:05:01 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:01:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:10:01 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:20 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 19:04:25 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:02:59 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:01:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:47 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:17:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 20:04:49 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.009 |  |
| 2026-06-15 20:03:08 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:01:47 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:05:30 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:00:42 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:05:38 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-06-15 20:06:06 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-15 20:07:34 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-15 20:04:38 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.020 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-15 20:05:36 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-15 20:05:55 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.032 |  |
| 2026-06-15 20:05:03 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.033 |  |
| 2026-06-15 20:02:51 | Ellagawa (Kalu Ganga) | 5.91 | 🟢 Normal | -0.039 |  |
| 2026-06-15 20:03:11 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-06-15 20:02:41 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-06-15 20:00:15 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.063 |  |
| 2026-06-15 20:08:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.067 |  |
| 2026-06-15 20:04:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)