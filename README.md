# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_05:04:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 05:04:13 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:04:02 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-01-10 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:03:57 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-01-10 05:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:03:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 05:03:19 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:03:03 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.202 |  |
| 2026-01-10 05:02:59 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:02:55 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:54 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:53 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:52 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:50 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-01-10 05:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-01-10 05:02:20 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-10 05:02:18 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 05:02:03 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:37 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 05:01:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.015 |  |
| 2026-01-10 04:56:07 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:39:52 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:32:17 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:30:06 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:28:31 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 04:23:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:20:44 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:15:25 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.017 |  |
| 2026-01-10 04:13:17 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-10 04:07:41 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-10 04:07:30 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 04:06:33 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 13.846 | 🔺 Rising |
| 2026-01-10 04:13:17 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-10 04:02:29 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-10 05:03:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-10 05:02:20 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-10 02:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-10 05:01:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 05:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 03:08:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:02:18 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 05:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:30:06 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:40:52 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:23:34 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:03 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:07:30 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:01:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:01:37 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:37 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:04:13 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:39:52 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:32:17 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 04:20:44 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 05:02:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.004 |  |
| 2026-01-10 05:04:02 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-01-10 04:07:41 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-10 04:01:17 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.012 |  |
| 2026-01-10 05:01:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.015 |  |
| 2026-01-10 04:15:25 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.017 |  |
| 2026-01-10 05:03:57 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-01-10 04:01:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-01-10 04:06:24 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-01-10 05:03:03 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.202 |  |
| 2026-01-10 05:03:19 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -7.200 |  |
| 2026-01-10 05:02:55 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)