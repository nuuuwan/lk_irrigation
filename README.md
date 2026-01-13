# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_04:07:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 04:07:33 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:35 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-14 04:06:24 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:06:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-01-14 04:05:39 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-01-14 04:05:22 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | -144.000 |  |
| 2026-01-14 04:05:20 | Horowpothana (Yan Oya) | 3.62 | 🟢 Normal | -144.000 |  |
| 2026-01-14 04:05:19 | Horowpothana (Yan Oya) | 3.67 | 🟢 Normal | -144.000 |  |
| 2026-01-14 04:05:18 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:03 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:00 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:04:23 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:54 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.024 |  |
| 2026-01-14 04:03:22 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:03:06 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:33 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:13 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:07 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:02:01 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.189 |  |
| 2026-01-14 04:01:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:17 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:00:52 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:00:51 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:00:09 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-14 03:55:52 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:53:41 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:19:43 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:15:52 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -1.846 |  |
| 2026-01-14 03:15:13 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | -1.846 |  |
| 2026-01-14 03:14:59 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:14:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.071 |  |
| 2026-01-14 03:14:21 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:14:17 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.189 |  |
| 2026-01-14 03:14:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-01-14 03:13:43 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-01-14 03:12:58 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.024 |  |
| 2026-01-14 03:11:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-14 03:10:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 03:14:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-01-14 03:00:47 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-14 04:06:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-14 01:06:49 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 03:08:22 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-14 03:06:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.004 |  |
| 2026-01-14 04:01:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:07:33 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:54 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:00 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:06 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:18 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:33 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:07 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:02:13 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:05:03 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:06:35 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:11:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-14 04:06:24 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:03:22 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:02:07 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:01:17 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:00:52 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-14 04:05:39 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-14 04:00:09 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-14 04:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.024 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-14 04:06:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.071 |  |
| 2026-01-14 04:02:01 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.189 |  |
| 2026-01-14 03:15:52 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -1.846 |  |
| 2026-01-14 02:10:26 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -36.000 |  |
| 2026-01-14 04:05:22 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)