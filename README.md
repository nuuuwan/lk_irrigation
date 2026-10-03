# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_02:28:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 02:28:43 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:27:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-04 02:22:31 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:20:06 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.023 |  |
| 2026-10-04 02:08:41 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:07:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:07:00 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:06:53 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-10-04 02:05:58 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-10-04 02:05:52 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-04 02:05:17 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:04:28 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-04 02:03:31 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-04 02:03:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-10-04 02:03:07 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-04 02:02:46 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.061 |  |
| 2026-10-04 02:02:42 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 02:02:29 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:02:22 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:02:14 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | -0.080 |  |
| 2026-10-04 02:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:58 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:43 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:38 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 02:01:36 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:33 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:25 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.061 |  |
| 2026-10-04 02:00:49 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:00:49 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:00:43 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | -0.041 |  |
| 2026-10-04 02:00:29 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 02:04:28 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-04 02:03:31 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-04 02:27:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-04 01:04:21 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-04 02:05:52 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-04 01:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 02:01:38 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 02:02:42 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 02:02:29 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:08:41 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 02:00:49 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:58 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:22:31 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:01:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:00:29 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:36 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:28:43 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:07:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:05:17 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:00:49 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:43 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:01:33 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 02:05:58 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-10-04 02:03:07 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 01:11:08 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-10-04 02:03:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-10-04 02:20:06 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.023 |  |
| 2026-10-04 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-10-04 02:06:53 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2026-10-04 01:46:07 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-10-04 02:00:43 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | -0.041 |  |
| 2026-10-04 02:02:46 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.061 |  |
| 2026-10-04 02:01:25 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.061 |  |
| 2026-10-04 02:02:14 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)