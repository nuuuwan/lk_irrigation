# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_05:28:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,875 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 05:28:51 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -0.103 |  |
| 2026-02-20 05:23:58 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 05:23:20 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-20 05:22:06 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:18:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-20 05:16:34 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-20 05:13:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-20 05:12:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:12:25 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-20 05:11:22 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 05:10:05 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -36.000 |  |
| 2026-02-20 05:10:04 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -36.000 |  |
| 2026-02-20 05:09:22 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-02-20 05:08:09 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:06:06 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-20 05:05:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:04:53 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-20 05:04:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 05:04:06 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 05:03:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:03:25 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-02-20 05:03:22 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.099 |  |
| 2026-02-20 05:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:02:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.035 |  |
| 2026-02-20 05:02:33 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 05:02:25 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-02-20 05:02:23 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 05:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:01:45 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:01:44 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:01:21 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-20 05:01:19 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.042 |  |
| 2026-02-20 05:01:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:00:58 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:00:20 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:47:05 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.042 |  |
| 2026-02-20 04:42:45 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 05:16:34 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-20 05:12:25 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-20 05:04:53 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-20 05:03:25 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-02-20 05:01:21 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-20 05:18:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-20 05:04:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 05:02:33 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 05:11:22 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-20 05:02:23 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 05:04:06 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 05:23:58 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 05:23:20 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-20 05:22:06 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:00:20 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:00:58 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 04:03:45 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:03:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 23:12:07 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:12:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:05:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:01:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:01:44 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 05:09:22 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-02-20 05:13:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-20 05:06:06 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-02-20 05:08:09 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:01:45 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-20 05:02:25 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-02-20 05:02:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.035 |  |
| 2026-02-20 05:01:19 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.042 |  |
| 2026-02-20 05:03:22 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.099 |  |
| 2026-02-20 05:28:51 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -0.103 |  |
| 2026-02-20 05:10:05 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)