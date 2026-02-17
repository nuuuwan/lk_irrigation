# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_17:14:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 17:14:29 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-02-17 17:14:17 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:14:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:13:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:09:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-02-17 17:08:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.117 |  |
| 2026-02-17 17:08:28 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-17 17:07:51 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:06:39 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:06:08 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 17:05:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:04:19 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:04:04 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 17:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:03:41 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:03:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-17 17:03:15 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-17 17:03:03 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:03:02 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.092 |  |
| 2026-02-17 17:02:43 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:39 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:32 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:31 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-17 17:02:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:19 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:19 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-17 17:02:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:10 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:01:55 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 17:01:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:42 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:40 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:33 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:26 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:00 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:00:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 17:03:15 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-17 17:02:19 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-17 17:06:08 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 17:04:04 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 17:01:55 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 17:00:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:00 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:40 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:08:28 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:03:03 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:06:39 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:32 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:42 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:14:17 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:04:19 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:02:39 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:07:51 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:05:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:01:33 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:14:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:13:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 17:14:29 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-02-17 17:02:10 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:03:41 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:19 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:02:43 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:01:26 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-17 17:03:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-17 17:02:31 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-17 17:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-17 17:09:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-02-17 17:03:02 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.092 |  |
| 2026-02-17 17:08:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)