# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_00:16:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 00:16:31 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-07 00:15:01 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.033 |  |
| 2026-10-07 00:14:49 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-07 00:11:40 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-10-07 00:08:57 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.082 |  |
| 2026-10-07 00:06:59 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-10-07 00:06:55 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-07 00:06:29 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:06:11 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 00:06:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:05:34 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-07 00:05:33 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-10-07 00:03:46 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:03:45 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-07 00:03:41 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-07 00:03:37 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.631 | 🔺 Rising |
| 2026-10-07 00:03:32 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 00:03:29 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:03:26 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-10-07 00:03:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.080 |  |
| 2026-10-07 00:03:01 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-07 00:02:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:02:28 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-10-07 00:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:02:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:52 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-07 00:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:27 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.005 |  |
| 2026-10-07 00:00:39 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 00:03:37 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.631 | 🔺 Rising |
| 2026-10-07 00:11:40 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-10-06 23:06:14 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 23:08:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-07 00:03:32 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 00:05:34 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-07 00:06:55 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-07 00:06:11 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 00:14:49 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-07 00:16:31 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-07 00:03:45 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-07 00:00:39 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 00:01:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.005 |  |
| 2026-10-07 00:02:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:27 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:52 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:06:00 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:03:46 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:06:59 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-10-06 23:04:09 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:03:29 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:06:29 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-10-07 00:02:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-07 00:05:33 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-10-07 00:03:41 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-07 00:03:01 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-07 00:03:26 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-10-07 00:02:28 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-10-07 00:15:01 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.033 |  |
| 2026-10-07 00:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-07 00:03:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.080 |  |
| 2026-10-07 00:08:57 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)